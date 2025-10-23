# code calculates balance between sick and healthy people given the starting numbers and falling sick/getting healthy ratios



# sposób 1 (najszybszy), zwraca liczbę zdrowych i chorych osób w równowadze

def balans(healthy_number, sick_number, falling_sick_rate, getting_healthy_rate):
    total = healthy_number + sick_number # suma chorych i zdrowych
    ratio = falling_sick_rate / getting_healthy_rate # ratio chorowania do zdrowienia
    healthy_final = total / (1 + ratio) # finalna liczba osob zdrowych
    sick_final = total - healthy_final # finalna liczba chorych
    return healthy_final, sick_final

# użycie funkcji
balans(150, 120, 0.2, 0.1)

# sposób 2 (pozwala na obsłużenie większej liczby stanów)
# dane podaje się poprzez inputy po wywołaniu funkcji

def balans_2(tolerance=1e-6, max_iterations=1000):
    # liczba stanów (np chory zdrowy)
    n = int(input("Podaj liczbę stanów: "))
    
    # liczba osób inputy i error handling
    initial = []
    for i in range(n):
        while True:
            try:
                val = int(input(f"Podaj liczbę osób w stanie {i+1} ≥0: "))
                if val < 0:
                    raise ValueError
                initial.append(val)
                break
            except ValueError:
                print("Niepoprawna wartość. Podaj liczbę całkowitą >= 0.")
    print("Początkowe liczby osób:", initial)
    
    # input macierzy przejścia i error handling
    transition = []
    for i in range(n):
        row = []
        print(f"wprowadź prawdopodobieństwa zmiany stanu z {i+1}:")
        while True:
            try:
                row_input = input(f"  wprowadź {n} wartości, oddziel je spacją ").split()
                if len(row_input) != n:
                    raise ValueError("niepoprawna liczba wartości")
                row = [float(x) for x in row_input]
                if any(x < 0 or x > 1 for x in row):
                    raise ValueError("każde prawdopodobieństwo musi być od 0 do 1")
                if abs(sum(row) - 1) > 1e-6:
                    raise ValueError("suma prawdopodobieństw musi wynosić 1")
                break
            except ValueError as e:
                print("błąd", e)
        transition.append(row)
    print("macierz przejścia:")
    for row in transition:
        print(row)
    
    # obliczanie rozkładu stacjonarnego (iterujemy stany po kolei)
    total = sum(initial)
    v = [x / total for x in initial]
    
    for _ in range(max_iterations):
        v_new = [0.0] * n    # nowy wektor prawdopodobieństw
        # przemnażamy wektor starych stanów przez macierz przejść
        for i in range(n):   # po każdym stanie początkowym
            for j in range(n):    # po każdym stanie docelowym
                v_new[j] += v[i] * transition[i][j]     # dodajemy udział przejścia i ==> j
        
        # test jak bardzo zmienił się rozkład między iteracjami
        diff = sum(abs(v_new[i] - v[i]) for i in range(n))
        v = v_new # aktualizacja wektora
        if diff < tolerance:   # sprawdzamy czy zmiana jest mniejsza niż tolerancja
            break
    
    v_final = [x * total for x in v]   # wracamy do liczby osób
    print("rozkład:", v_final)

# Wywołanie funkcji
balans_2()