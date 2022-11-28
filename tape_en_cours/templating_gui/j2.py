# -*- coding: utf-8 -*-

import itertools

TO_REPLACE_K1 = "xk1x"
TO_REPLACE_K2 = "xk2x"

# print("dans j2", __name__)

k1s = [1e1, 2e2, 3e3, 3.4]
k2s = [80_000, 900_000, 1_000_000]


def create_one_file(fname_to_create, template, TO_REPLACE_K1, TO_REPLACE_K2, k1, k2):
    print(fname_to_create)
    with open(fname_to_create, "w") as f_new:
        res = template.replace(TO_REPLACE_K1, str(k1)).replace(TO_REPLACE_K2, str(k2))
        f_new.write(res)


def shout(word):
    shouted_word = word.upper()
    return shouted_word


print(shout("enough!"))


def run(fname, TO_REPLACE_K1, TO_REPLACE_K2, k1s, k2s):
    template = open(fname).read()

    for index, (k1, k2) in enumerate(
        itertools.zip_longest(k1s, k2s, fillvalue=7), start=1
    ):
        f_name = "fichier_simu_{}.txt".format(index)
        create_one_file(f_name, template, TO_REPLACE_K1, TO_REPLACE_K2, k1, k2)


def get_file_name():
    fname = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(
            ("TXT files", "*.txt"),
            ("CSV files", "*.csv"),
            ("all files", "*.*"),
        ),
    )
    return fname


def main():
    fname = get_file_name()
    print(f"le template est {fname}")
    run(fname)


if __name__ == "__main__":
    main()
