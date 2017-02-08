# -*- coding: utf-8 -*-
from typing import (Generic, ItemsView, Iterable, Iterator, KeysView, Mapping, Hashable,
                    MutableMapping, Optional, Set, Type, TypeVar, Union, ValuesView, overload)

T = TypeVar('T')
TElement = TypeVar('TElement', bound=Hashable)
OtherType = Union[Iterable[TElement], Mapping[TElement, int]]
Self = TypeVar('Self', bound='BaseMultiset')

class BaseMultiset(Mapping[TElement, int], Generic[TElement]):
    def __init__(self, iterable: Optional[OtherType]=None) -> None: ...
    def __new__(cls, iterable=None): ...
    def __contains__(self, element: object) -> bool: ...
    def __getitem__(self, element: TElement) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TElement]: ...
    def isdisjoint(self, other: OtherType) -> bool: ...
    def difference(self: Self, *others: OtherType) -> Self: ...
    @overload
    def __sub__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __sub__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    def union(self: Self, *others: OtherType) -> Self: ...
    @overload
    def __or__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __or__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    __ror__ = __or__
    def combine(self: Self, *others: OtherType) -> Self: ...
    @overload
    def __add__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __add__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    __radd__ = __add__
    def intersection(self: Self, *others: OtherType) -> Self: ...
    @overload
    def __and__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __and__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    __rand__ = __and__
    def symmetric_difference(self: Self, other: OtherType) -> Self: ...
    @overload
    def __xor__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __xor__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    __rxor__ = __xor__
    def times(self: Self, factor: int) -> Self: ...
    def __mul__(self: Self, factor: int) -> Self: ...
    __rmul__ = __mul__
    def _issubset(self, other: OtherType, strict: bool) -> bool: ...
    def issubset(self, other: OtherType) -> bool: ...
    @overload
    def __le__(self, other: Set[TElement]) -> bool: ...
    @overload
    def __le__(self, other: 'BaseMultiset[TElement]') -> bool: ...
    @overload
    def __lt__(self, other: Set[TElement]) -> bool: ...
    @overload
    def __lt__(self, other: 'BaseMultiset[TElement]') -> bool: ...
    def _issuperset(self, other: OtherType, strict: bool) -> bool: ...
    def issuperset(self, other: OtherType) -> bool: ...
    @overload
    def __ge__(self, other: Set[TElement]) -> bool: ...
    @overload
    def __ge__(self, other: 'BaseMultiset[TElement]') -> bool: ...
    @overload
    def __gt__(self, other: Set[TElement]) -> bool: ...
    @overload
    def __gt__(self, other: 'BaseMultiset[TElement]') -> bool: ...
    def __eq__(self, other: object): ...
    def __ne__(self, other: object): ...
    def get(self, element: TElement, default: int) -> int: ... # type: ignore
    @classmethod
    def from_elements(cls: Type[Self], elements: Iterable[TElement], multiplicity: int) -> Self: ...
    def copy(self: Self) -> Self: ...
    def __copy__(self: Self) -> Self: ...
    def items(self) -> ItemsView[TElement, int]: ...
    def distinct_elements(self) -> KeysView[TElement]: ...
    def multiplicities(self) -> ValuesView[int]: ...

class Multiset(BaseMultiset[TElement], MutableMapping[TElement, int], Generic[TElement]):
    def __setitem__(self, element: TElement, multiplicity: int) -> None: ...
    def __delitem__(self, element: TElement) -> None: ...
    def update(self, *others: OtherType) -> None: ...
    def union_update(self, *others: OtherType) -> None: ...
    @overload
    def __ior__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __ior__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    def intersection_update(self, *others: OtherType) -> None: ...
    @overload
    def __iand__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __iand__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    def difference_update(self, *others: OtherType) -> None: ...
    @overload
    def __isub__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __isub__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    def symmetric_difference_update(self, other: OtherType) -> None: ...
    @overload
    def __ixor__(self: Self, other: Set[TElement]) -> Self: ...
    @overload
    def __ixor__(self: Self, other: 'BaseMultiset[TElement]') -> Self: ...
    def times_update(self, factor: int) -> None: ...
    def __imul__(self: Self, factor: int) -> Self: ...
    def add(self, element: TElement, multiplicity: int=1) -> None: ...
    def remove(self, element: TElement, multiplicity: Optional[int]=None) -> int: ...
    def discard(self, element: TElement, multiplicity: Optional[int]=None) -> int: ...
    def pop(self, element: TElement, default: int) -> int: ... # type: ignore
    def setdefault(self, element: TElement, default: int) -> int: ... # type: ignore
    def clear(self) -> None: ...

class FrozenMultiset(BaseMultiset[TElement], Generic[TElement]):
    def __hash__(self): ...
