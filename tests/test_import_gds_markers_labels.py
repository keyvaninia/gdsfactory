from __future__ import annotations

import json

import pandas as pd

import gdsfactory as gf


def test_import_json_label(data_regression) -> None:
    """Make sure you can import the ports"""
    c = gf.components.straight(
        decorator=gf.add_pins.add_pins_siepic, cross_section="xs_sc_no_pins"
    )
    c1 = gf.functions.rotate(
        gf.routing.add_fiber_single(c), angle=90, decorator=gf.labels.add_label_json
    )
    gdspath = c1.write_gds()
    csvpath = gf.labels.write_labels.write_labels_gdstk(gdspath, prefixes=("{",))
    labels = pd.read_csv(csvpath)

    settings = json.loads(labels.text[0])
    data_regression.check(settings)


if __name__ == "__main__":
    c = gf.components.straight(
        decorator=gf.add_pins.add_pins_siepic, cross_section="xs_sc_no_pins"
    )
    c1 = gf.functions.rotate(
        gf.routing.add_fiber_single(c), angle=90, decorator=gf.labels.add_label_json
    )
    gdspath = c1.write_gds()
    csvpath = gf.labels.write_labels.write_labels_gdstk(gdspath, prefixes=("{",))
    labels = pd.read_csv(csvpath)
    print(labels.text[0])
    settings = json.loads(labels.text[0])
    # settings = yaml.safe_load(labels.text[0])
    # c1.show()
