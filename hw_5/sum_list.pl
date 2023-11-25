% sum_list.pl

% Определение базового случая для пустого списка
sum_list([], 0).

% Рекурсивное вычисление суммы головы списка и суммы хвоста
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.