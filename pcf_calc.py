import sys


def calc_p(w_no_fat):
    p_gram = w_no_fat * 3.0
    p_kcal = p_gram * 4
    return p_gram, p_kcal


def calc_f(w_no_fat):
    f_gram = w_no_fat * 0.7
    f_kcal = f_gram * 9
    return f_gram, f_kcal


def calc_c(base, p_kcal, f_kcal):
    c_kcal = base - (p_kcal + f_kcal)
    c_gram = c_kcal / 4
    return c_gram, c_kcal


def main():
    argv = sys.argv
    weight = float(argv[1])
    fat_rate = float(argv[2])
    w_no_fat = weight * (1 - fat_rate)
    base_kcal = w_no_fat * 40

    p_gram, p_kcal = calc_p(w_no_fat)
    f_gram, f_kcal = calc_f(w_no_fat)
    c_gram, c_kcal = calc_c(base_kcal, p_kcal, f_kcal)

    print("P: {0:7.2f}g, {1:7.2f}kcal".format(p_gram, p_kcal))
    print("F: {0:7.2f}g, {1:7.2f}kcal".format(f_gram, f_kcal))
    print("C: {0:7.2f}g, {1:7.2f}kcal".format(c_gram, c_kcal))


if __name__ == "__main__":
    main()
