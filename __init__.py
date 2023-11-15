from dagster import Definitions, load_assets_from_modules
from assets import example_pipe

defs = Definitions(
    assets=load_assets_from_modules([example_pipe])
)