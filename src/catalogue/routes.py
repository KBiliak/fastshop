from src.common.routes import BaseCrudPrefixes


class CatalogueRoutesPrefixes:
    product: str = '/product'


class ProductRoutesPrefixes(BaseCrudPrefixes):
    search: str = '/search'
    update_index: str = '/update-index'
