# -*- coding: utf-8 -*-
"""Google Data Analytics: Python fundamentals (Module 1 to 3).

Runs the key exercises from the course labs end to end:
syntax and data types, functions, conditional statements,
while loops, for loops, and strings. Saves charts and findings.
"""
import json
import os
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(BASE, "charts")
DATA = os.path.join(BASE, "data")

plt.rcParams.update({"figure.dpi": 130, "font.size": 10})


def savefig(name, title, xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS, name))
    plt.close()


# ---------- 1. Syntax and data types ----------
def syntax_demo():
    course = "Python"
    version = 3
    rating = 4.8
    is_fun = True
    print("course:", course, type(course).__name__)
    print("version:", version, type(version).__name__)
    print("rating:", rating, type(rating).__name__)
    print("is_fun:", is_fun, type(is_fun).__name__)
    as_string = str(version)
    as_int = int(4.8)
    print("str(3):", as_string, "| int(4.8):", as_int)
    return {"course": course, "version": version}


# ---------- 2. Functions ----------
def greet(name):
    return "Halo, " + name + "! Selamat belajar Python."


def circle_area(radius):
    pi = 3.14159
    return pi * radius * radius


# ---------- 3. Conditional statements ----------
def comparator(a, b):
    if a > b:
        return "a lebih besar"
    elif a < b:
        return "b lebih besar"
    else:
        return "sama besar"


def grade_label(score):
    if score >= 9:
        return "positif"
    elif score >= 6:
        return "netral"
    else:
        return "negatif"


# ---------- 4. While loop ----------
def countdown(start):
    values = []
    n = start
    while n > 0:
        values.append(n)
        n -= 1
    return values


def webpage_timer(seconds):
    ticks = []
    remaining = seconds
    while remaining > 0:
        ticks.append(remaining)
        remaining -= 1
    ticks.append("selesai")
    return ticks


# ---------- 5. For loops (exemplar solutions) ----------
def score_counter(score_list):
    negative_scores = 0
    neutral_scores = 0
    positive_scores = 0
    for score in score_list:
        if score >= 9:
            positive_scores += 1
        elif score >= 6:
            neutral_scores += 1
        else:
            negative_scores += 1
    return {"negatif": negative_scores, "netral": neutral_scores,
            "positif": positive_scores}


def id_validator(verified_ids, feedback_ids):
    unverified_feedback = 0
    for fid in feedback_ids:
        if fid not in verified_ids:
            unverified_feedback += 1
    percent = unverified_feedback / len(feedback_ids) * 100
    return {"unverified": unverified_feedback, "total": len(feedback_ids),
            "percent": round(percent, 2)}


# ---------- 6. Strings ----------
def concat_demo(first, last):
    return first + " " + last


def extract_store_id(code):
    # format contoh: "TOKO/042/BALI" : ambil angka di tengah
    parts = code.split("/")
    return parts[1]


def string_report(text):
    return {
        "panjang": len(text),
        "kata": len(text.split()),
        "kapital": text.upper(),
        "apakah_alfabet": text.replace(" ", "").isalpha(),
    }


def main():
    findings = {}

    print("== 1. Sintaks dan tipe data ==")
    findings["syntax"] = syntax_demo()

    print("== 2. Fungsi ==")
    print(greet("Baghiz"))
    print("Luas lingkaran r=5:", round(circle_area(5), 2))
    findings["circle_area_r5"] = round(circle_area(5), 2)

    print("== 3. Kondisional ==")
    for a, b in [(10, 4), (3, 8), (7, 7)]:
        print(a, "vs", b, "=", comparator(a, b))

    print("== 4. While loop ==")
    cd = countdown(5)
    print("countdown:", cd)
    print("timer:", webpage_timer(3))
    findings["countdown_5"] = cd
    plt.figure(figsize=(6, 3.5))
    plt.plot(range(1, len(cd) + 1), cd, marker="o")
    savefig("01_countdown.png", "Countdown While Loop",
            "Langkah", "Nilai")
    squares = [i * i for i in range(1, 11)]
    plt.figure(figsize=(6, 3.5))
    plt.bar(range(1, 11), squares, color="#1D4ED8")
    savefig("02_for_squares.png", "For Loop: Kuadrat 1 sampai 10",
            "Angka", "Kuadrat")

    print("== 5. For loop: score_counter ==")
    random.seed(42)
    possible_scores = list(range(1, 11))
    score_list = random.choices(
        possible_scores, weights=[8, 8, 8, 8, 8, 3, 3, 4, 20, 30], k=200)
    sentiments = score_counter(score_list)
    print(sentiments)
    findings["sentiments_200"] = sentiments
    labels = ["negatif", "netral", "positif"]
    plt.figure(figsize=(6, 3.5))
    plt.bar(labels, [sentiments[k] for k in labels],
            color=["#DC2626", "#F59E0B", "#16A34A"])
    savefig("03_sentimen.png", "Hasil score_counter: 200 Skor Feedback",
            "Sentimen", "Jumlah")

    print("== 5b. For loop: id_validator ==")
    random.seed(7)
    verified = random.sample(range(1000, 2000), 80)
    feedback = random.choices(range(1000, 2000), k=120)
    val = id_validator(verified, feedback)
    print(val["unverified"], "dari", val["total"], "ID tidak terverifikasi.")
    print(str(val["percent"]) + "% tidak terverifikasi.")
    findings["id_validation"] = val
    plt.figure(figsize=(6, 3.5))
    plt.bar(["terverifikasi", "tidak terverifikasi"],
            [val["total"] - val["unverified"], val["unverified"]],
            color=["#16A34A", "#DC2626"])
    savefig("04_validasi_id.png", "Validasi ID Feedback",
            "Status", "Jumlah")

    print("== 6. String ==")
    print(concat_demo("Baghiz", "Arasya"))
    print("Store ID:", extract_store_id("TOKO/042/BALI"))
    rep = string_report("belajar python itu seru")
    print(rep)
    findings["string_report"] = rep
    findings["store_id"] = extract_store_id("TOKO/042/BALI")

    with open(os.path.join(BASE, "findings.json"), "w") as f:
        json.dump(findings, f, indent=2, ensure_ascii=False)
    print("Selesai. Chart tersimpan di charts/.")


if __name__ == "__main__":
    main()
