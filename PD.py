import time
import matplotlib.pyplot as plt

# Word Break con Programación Dinámica
def wordBreakDP(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]

# Tests normales
tests = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
    ("abcd", ["a", "abc", "b", "cd"]),
    ("aaaaaaaaaa", ["a", "aa", "aaa"]),
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
    ("aaaaaaa", ["aa", "aaa"]),
    ("bbbaaa", ["b", "bb", "a", "aa"]),
    ("xyzxyzxyz", ["x", "y", "z", "xy", "xyz"]),
    ("abacaba", ["a", "ba", "bac", "ab", "caba"]),
    ("helloworld", ["hello", "world"]),
    ("iliketoplay", ["i", "like", "to", "play"]),
    ("aaaaaaa", ["a", "aa", "aaa", "aaaa"]),
    ("abcabcabc", ["a", "b", "c", "ab", "bc", "abc"]),
    ("superman", ["super", "man"]),
    ("cancancan", ["can", "c", "a", "n"]),
    ("zzzzzzz", ["z", "zz", "zzz"]),
    ("programmingisfun", ["programming", "is", "fun"]),
    ("openaiisawesome", ["open", "ai", "is", "awesome"]),
    ("aaaaaaaaaaaaaaaa", ["a", "aa", "aaa", "aaaa"]),
    ("hacktheplanet", ["hack", "the", "planet"]),
    ("testcasetest", ["test", "case"]),
    ("eatsleepcode", ["eat", "sleep", "code"]),
    ("lalalalalalalalala", ["la", "lala"]),
    ("blockchain", ["block", "chain"]),
    ("bitcoindoge", ["bitcoin", "doge"]),
    ("letscodeinpython", ["let", "code", "in", "python"]),
    ("datastructures", ["data", "structures"]),
    ("machinelearning", ["machine", "learning"])
]

# Test difíciles
difficult_test = [
    ("a" * 20 + "b", ["a", "aa", "aaa", "aaaa", "aaaaa"]),
    ("a" * 25, ["a", "aa", "aaa", "aaaa", "aaaaa"]),
    ("ab" * 15, ["a", "ab", "b"]),
    ("abababababababababababababababab", ["ab", "a", "b", "aba"]),
    ("xyz" * 10 + "x", ["x", "y", "z", "xy", "yz", "xyz"]),
    ("catcatcatdogdog", ["cat", "dog", "catdog", "dogcat"]),
    ("pineapplepineapplepenpineapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
    ("a" * 47, ["a", "aa", "aaa"]),
    ("abcd" * 10, ["a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", "abcd"]),
    ("letscodeinpythonandjava", ["let", "lets", "code", "in", "python", "java", "and"])
]

tests.extend(difficult_test)

# Medición de tiempo
tiempos_individuales = []
tiempos_acumulados = []
acumulado = 0

print("Caso\t\t\t\t\tTiempo (ms)\tResultado")
print("---------------------------------------------------------------")

for s, wordDict in tests:
    inicio = time.perf_counter()
    resultado = wordBreakDP(s, wordDict)
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000
    acumulado += tiempo_ms

    tiempos_individuales.append(tiempo_ms)
    tiempos_acumulados.append(acumulado)

    print(f"{s[:30]:<30}\t{tiempo_ms:.6f}\t{resultado}")

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(tiempos_acumulados) + 1), tiempos_acumulados, marker='o', color='green')
plt.title("Tiempo acumulado de ejecución - Word Break con Programación Dinámica")
plt.xlabel("Número de caso")
plt.ylabel("Tiempo acumulado (ms)")
plt.grid(True)
plt.tight_layout()
plt.show()
