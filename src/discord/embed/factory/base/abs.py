from discord import Embed

from abc import ABCMeta, abstractmethod


class AbstractEmbedFactory(metaclass=ABCMeta):
    @abstractmethod
    def make(self) -> Embed:
        NotImplementedError()
