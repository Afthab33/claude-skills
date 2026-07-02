#!/usr/bin/env python3
"""WCAG color-contrast checker.

Verify foreground/background pairs meet WCAG 2.x contrast minimums BEFORE
shipping an HTML page. This is the deterministic guard against the most common
failure: text that "looks fine" to the author but is unreadable.

Usage:
    python contrast.py "#1f2d3a" "#f4f6f7"                  # one pair
    python contrast.py "#1f2d3a/#f4f6f7" "#5c6b76/#f4f6f7"  # many pairs
    python contrast.py --large "#8595a0" "#ffffff"          # large-text thresholds

Thresholds (contrast ratio):
    Normal text  — AA 4.5  | AAA 7.0
    Large text   — AA 3.0  | AAA 4.5   (>=24px, or >=18.66px bold)
    UI / borders — 3.0     (non-text contrast)

Exit code is non-zero if any pair fails AA, so it can gate a build.
"""
import sys


def _to_lin(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexstr: str) -> float:
    h = hexstr.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) != 6:
        raise ValueError(f"bad hex color: {hexstr!r}")
    r, g, b = (int(h[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _to_lin(r) + 0.7152 * _to_lin(g) + 0.0722 * _to_lin(b)


def ratio(fg: str, bg: str) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def main(argv: list[str]) -> int:
    large = False
    args = []
    for a in argv:
        if a in ("--large", "-l"):
            large = True
        else:
            args.append(a)

    pairs = []
    i = 0
    while i < len(args):
        if "/" in args[i]:
            fg, bg = args[i].split("/", 1)
            pairs.append((fg, bg))
            i += 1
        else:
            if i + 1 >= len(args):
                print(f"unpaired color: {args[i]}", file=sys.stderr)
                return 2
            pairs.append((args[i], args[i + 1]))
            i += 2

    if not pairs:
        print(__doc__)
        return 2

    aa = 3.0 if large else 4.5
    aaa = 4.5 if large else 7.0
    worst_fail = False
    print(f"{'fg':>9} {'bg':>9} {'ratio':>7}  AA   AAA")
    print("-" * 40)
    for fg, bg in pairs:
        r = ratio(fg, bg)
        pass_aa = r >= aa
        pass_aaa = r >= aaa
        worst_fail |= not pass_aa
        mark = lambda ok: "PASS" if ok else "FAIL"
        print(f"{fg:>9} {bg:>9} {r:>6.2f}:1  {mark(pass_aa):<4} {mark(pass_aaa)}")
    print("-" * 40)
    print(f"thresholds: AA>={aa}  AAA>={aaa}  ({'large' if large else 'normal'} text)")
    if worst_fail:
        print("\nFAIL: at least one pair is below AA. Darken/lighten until it passes.")
    return 1 if worst_fail else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
