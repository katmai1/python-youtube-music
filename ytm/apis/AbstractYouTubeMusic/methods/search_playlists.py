from .. import decorators

# @decorators.method(__method__)
@decorators.method()
def search_playlists(self: object, query: str) -> list:
    return self._search_filter(query, 'playlists')