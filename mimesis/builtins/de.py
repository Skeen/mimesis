# -*- coding: utf-8 -*-

"""Specific data provider for Germany (de)."""

from typing import List, Optional

from mimesis import locales
from mimesis.builtins.base import BaseSpecProvider
from mimesis.typing import Seed

__all__ = ['GermanySpecProvider']


class GermanySpecProvider(BaseSpecProvider):
    """Specific-provider of misc data for Germany."""

    def __init__(self, seed: Optional[Seed] = None):
        """Initialize attributes."""
        super().__init__(locale=locales.DE, seed=seed)
        self._pull(self._datafile)

    class Meta:
        """The name of the provider."""

        name = 'germany_provider'

    def noun(self, plural: bool = False) -> str:
        """Return a random noun in German.

        :param plural: Return noun in plural.
        :return: Noun.
        """
        key = 'plural' if \
            plural else 'noun'
        nouns: List[str] = self._data[key]
        return self.random.choice(nouns)
