from abc import ABC, abstractmethod


class IConnectionDatabase(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def run_query(self) -> None:
        pass

    @abstractmethod
    def confirm(self) -> None:
        pass
