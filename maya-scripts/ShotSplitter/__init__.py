from ShotSplitter.interface import show

from UkoreMenu import registry, MenuItemSpec, ReloadHandlerSpec, reload_package

registry.register_item(
    MenuItemSpec(
        id="shot_splitter",
        label="Shot Splitter...",
        category="Anim",
        command="import ShotSplitter; ShotSplitter.show()",
        order=20,
    )
)

registry.register_reload_handler(
    ReloadHandlerSpec(
        id="shot_splitter",
        label="ShotSplitter",
        callback=lambda: reload_package("ShotSplitter"),
        order=20,
    )
)

__all__ = ["show"]
