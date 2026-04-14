grades = {
    ("jon","math",):5,
    ("robert","haxhiu"):5
}

print(grades[("robert","haxhiu")])

grades[("jon","math")]=4

print(grades[("jon","math")])

suksesi =list(grades.values()
              )
print(suksesi)