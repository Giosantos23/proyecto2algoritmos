import time
import matplotlib.pyplot as plt



def wordBreakDAC(s, wordDict):
    if s == "":
        return True
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        suffix = s[i:]
        if prefix in wordDict and wordBreakDAC(suffix, wordDict):
            return True
    return False

if __name__ == "__main__":
    # Tests normales
    tests = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("abcd", ["a", "abc", "b", "cd"]),
        ("aaaaaaaaaa", ["a", "aa", "aaa"]),
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
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
    test_dificiles = [
        ("a" * 5 + "b", ["a", "aa", "aaa", "aaaa", "aaaaa"]), 
        ("a" * 7, ["a", "aa", "aaa", "aaaa", "aaaaa"]),     
        ("ab" * 10, ["a", "ab", "b"]),            
        ("abababababababababababababababab", ["ab", "a", "b", "aba"]), 
        ("xyz" * 8 + "x", ["x", "y", "z", "xy", "yz", "xyz"]),
        ("catcatcatdogdog", ["cat", "dog", "catdog", "dogcat"]),
        ("pineapplepineapplepenpineapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a", "aa", "aaa"]), 
        ("abcd" * 5, ["a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", "abcd"]),
        ("letscodeinpythonandjava", ["let", "lets", "code", "in", "python", "java", "and"])
    ]
    tests.extend(test_dificiles)

    tiempos_dac = []
    tiempos_acumulados = []
    total = 0



    print("Caso\t\t\t\t\tTiempo (ms)\t\t\tResultado")
    print("---------------------------------------------------------------")
    # Ejecutar pruebas y guardar tiempos
    for s, wordDict in tests:
        inicio = time.perf_counter()
        result = wordBreakDAC(s, set(wordDict))
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        total += tiempo_ms
        tiempos_dac.append(tiempo_ms)
        tiempos_acumulados.append(total)
        print(f"{s[:30]:<30}\t{tiempo_ms:.6f}\t{result}")
    
    # Gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(tiempos_acumulados) + 1), tiempos_acumulados, marker='o')
    plt.title("Tiempo acumulado de ejecución - Word Break DAC")
    plt.xlabel("Número de caso")
    plt.ylabel("Tiempo acumulado (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
