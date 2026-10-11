"""Pruebas del verificador de arquitectura. Ejecutar:
    python3 -m unittest discover -s tools/arch -v
"""
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_architecture as ca  # noqa: E402

CFG = {
    "version": 1,
    "root": "src",
    "layers": {
        "domain": [],
        "application": ["domain"],
        "infrastructure": ["application", "domain"],
        "presentation": ["application", "domain"],
        "api": ["application", "domain"],
    },
    "allowed_autoloads": ["App"],
    "domain_forbidden_symbols": ["Node", "Control", "Input", "FileAccess", "get_tree"],
    "modules": {
        "day": {"depends_on": []},
        "market": {"depends_on": ["day"]},
        "shop": {"depends_on": ["market"]},
    },
}


def build(files, cfg=None, project=None):
    tmp = tempfile.TemporaryDirectory()
    root = pathlib.Path(tmp.name)
    (root / "architecture.json").write_text(json.dumps(cfg or CFG), encoding="utf-8")
    for rel, text in files.items():
        p = root / "src" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    if project is not None:
        (root / "project.godot").write_text(project, encoding="utf-8")
    return tmp, root


def run(files, cfg=None, project=None):
    tmp, root = build(files, cfg, project)
    try:
        return ca.check(root)
    finally:
        tmp.cleanup()


class ReglasDeCapas(unittest.TestCase):
    def test_estructura_valida_no_da_errores(self):
        errors, _ = run({
            "kernel/result.gd": "class_name Result\nextends RefCounted\n",
            "modules/market/domain/price.gd": "class_name Price\nextends RefCounted\nvar r: Result\n",
            "modules/market/application/service.gd": "class_name MarketService\nextends RefCounted\nvar p: Price\n",
            "modules/market/presentation/view.gd": "extends Control\nvar s: MarketService\n",
            "modules/market/api/market_api.gd": "class_name MarketApi\nextends RefCounted\nvar s: MarketService\n",
            "modules/day/domain/clock.gd": "class_name Clock\nextends RefCounted\n",
            "modules/day/api/day_api.gd": "class_name DayApi\nextends RefCounted\n",
            "modules/shop/application/shop.gd": "extends RefCounted\nconst M = preload(\"res://src/modules/market/api/market_api.gd\")\n",
        })
        self.assertEqual(errors, [])

    def test_dominio_no_puede_usar_aplicacion(self):
        errors, _ = run({
            "modules/market/application/service.gd": "class_name MarketService\nextends RefCounted\n",
            "modules/market/domain/price.gd": "extends RefCounted\nvar s: MarketService\n",
        })
        self.assertTrue(any("A1" in e and "domain" in e for e in errors), errors)

    def test_presentacion_no_puede_usar_infraestructura(self):
        errors, _ = run({
            "modules/market/infrastructure/repo.gd": "class_name MarketRepo\nextends RefCounted\n",
            "modules/market/presentation/view.gd": "extends Control\nvar r: MarketRepo\n",
        })
        self.assertTrue(any("A1" in e for e in errors), errors)

    def test_modulo_no_puede_usar_internos_de_otro(self):
        errors, _ = run({
            "modules/day/domain/clock.gd": "class_name Clock\nextends RefCounted\n",
            "modules/market/application/service.gd": "extends RefCounted\nvar c: Clock\n",
        })
        self.assertTrue(any("A2" in e and "internos" in e for e in errors), errors)

    def test_api_de_otro_modulo_sin_declarar_falla(self):
        errors, _ = run({
            "modules/shop/api/shop_api.gd": "class_name ShopApi\nextends RefCounted\n",
            "modules/day/application/x.gd": "extends RefCounted\nconst S = preload(\"res://src/modules/shop/api/shop_api.gd\")\n",
        })
        self.assertTrue(any("sin declararlo" in e for e in errors), errors)

    def test_dominio_no_puede_depender_de_otro_modulo(self):
        errors, _ = run({
            "modules/day/api/day_api.gd": "class_name DayApi\nextends RefCounted\n",
            "modules/market/domain/p.gd": "extends RefCounted\nvar d: DayApi\n",
        })
        self.assertTrue(any("A3" in e for e in errors), errors)

    def test_comentarios_no_cuentan(self):
        errors, _ = run({
            "modules/day/domain/clock.gd": "class_name Clock\nextends RefCounted\n",
            "modules/market/application/s.gd": "extends RefCounted\n# usa Clock del módulo day\n",
        })
        self.assertEqual(errors, [])

    def test_cadenas_no_cuentan_como_clases(self):
        errors, _ = run({
            "modules/day/domain/clock.gd": "class_name Clock\nextends RefCounted\n",
            "modules/market/application/s.gd": "extends RefCounted\nvar t := \"Clock\"\n",
        })
        self.assertEqual(errors, [])


class ReglasDelDominio(unittest.TestCase):
    def test_dominio_no_usa_clases_del_motor(self):
        errors, _ = run({"modules/market/domain/p.gd": "extends Node\n"})
        self.assertTrue(any("A4" in e and "Node" in e for e in errors), errors)

    def test_dominio_no_usa_archivos_ni_entrada(self):
        errors, _ = run({"modules/market/domain/p.gd": "extends RefCounted\nfunc f():\n\tvar a = FileAccess.open(\"x\")\n\tInput.is_action_pressed(\"a\")\n"})
        self.assertEqual(len([e for e in errors if "A4" in e]), 2, errors)

    def test_presentacion_si_puede_usar_nodos(self):
        errors, _ = run({"modules/market/presentation/v.gd": "extends Control\n"})
        self.assertEqual(errors, [])


class ReglasDeNucleoYPlataforma(unittest.TestCase):
    def test_kernel_no_depende_de_modulos(self):
        errors, _ = run({
            "modules/day/domain/clock.gd": "class_name Clock\nextends RefCounted\n",
            "kernel/bus.gd": "extends RefCounted\nvar c: Clock\n",
        })
        self.assertTrue(any("A5" in e for e in errors), errors)

    def test_modulo_puede_usar_puertos_pero_no_adaptadores(self):
        errors, _ = run({
            "platform/ports/storage_port.gd": "class_name StoragePort\nextends RefCounted\n",
            "platform/adapters/file_storage.gd": "class_name FileStorage\nextends StoragePort\n",
            "modules/market/infrastructure/repo.gd": "extends RefCounted\nvar p: StoragePort\nvar a: FileStorage\n",
        })
        self.assertEqual(len([e for e in errors if "A6" in e]), 1, errors)
        self.assertFalse(any("StoragePort" in e for e in errors), errors)

    def test_dominio_no_usa_puertos(self):
        errors, _ = run({
            "platform/ports/storage_port.gd": "class_name StoragePort\nextends RefCounted\n",
            "modules/market/domain/p.gd": "extends RefCounted\nvar s: StoragePort\n",
        })
        self.assertTrue(any("A3" in e and "platform" in e for e in errors), errors)

    def test_app_puede_usarlo_todo(self):
        errors, _ = run({
            "platform/adapters/file_storage.gd": "class_name FileStorage\nextends RefCounted\n",
            "modules/market/application/s.gd": "class_name MarketService\nextends RefCounted\n",
            "app/composition.gd": "extends RefCounted\nvar a: FileStorage\nvar m: MarketService\n",
        })
        self.assertEqual(errors, [])


class ReglasDelGrafo(unittest.TestCase):
    def test_ciclo_entre_modulos(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["modules"]["day"]["depends_on"] = ["shop"]
        errors, _ = run({}, cfg)
        self.assertTrue(any("A7" in e for e in errors), errors)

    def test_modulo_sin_declarar(self):
        errors, _ = run({"modules/extra/domain/x.gd": "extends RefCounted\n"})
        self.assertTrue(any("A8" in e and "extra" in e for e in errors), errors)

    def test_dependencia_hacia_modulo_inexistente(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["modules"]["market"]["depends_on"] = ["fantasma"]
        errors, _ = run({"kernel/x.gd": "extends RefCounted\n"}, cfg)
        self.assertTrue(any("fantasma" in e for e in errors), errors)

    def test_autoload_no_permitido(self):
        project = "[application]\nname=\"x\"\n\n[autoload]\nApp=\"*res://src/app/app.gd\"\nGlobals=\"*res://src/globals.gd\"\n"
        errors, _ = run({"app/app.gd": "extends Node\n"}, None, project)
        self.assertEqual(len([e for e in errors if "A9" in e]), 1, errors)
        self.assertTrue(any("Globals" in e for e in errors), errors)

    def test_archivo_demasiado_largo_da_aviso(self):
        errors, warnings = run({"kernel/big.gd": "extends RefCounted\n" + "var x = 1\n" * 450})
        self.assertEqual(errors, [])
        self.assertTrue(any("líneas" in w for w in warnings), warnings)


class UtilidadesDeTexto(unittest.TestCase):
    def test_code_part_respeta_comillas(self):
        self.assertEqual(ca.code_part('var a = "x#y" # nota').rstrip(), 'var a = "x#y"')

    def test_blank_strings(self):
        self.assertEqual(ca.blank_strings('f("Clock") + g'), 'f("     ") + g')


if __name__ == "__main__":
    unittest.main()
