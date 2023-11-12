from dagster import Definitions, load_assets_from_modules, glob

defs = Definitions(
    assets=load_assets_from_modules(glob("assets/*.py"))
)