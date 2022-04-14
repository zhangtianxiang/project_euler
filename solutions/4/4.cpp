#include <cstdio>
#include <set>

std::set<int> palindroms;

char buf[16];

void check(int x) {
  int n = sprintf(buf, "%d", x);
  for (int i = (n / 2) - 1; i >= 0; i--) {
    if (buf[i] != buf[n - i - 1]) return;
  }
  palindroms.insert(x);
}

inline void pre() {
  for (int i = 100; i <= 999; i++) {
    for (int j = i; j <= 999; j++) {
      check(i * j);
    }
  }
}

inline void work() {
  int n;
  scanf("%d", &n);
  auto it = palindroms.lower_bound(n);
  it--;
  printf("%d\n", *it);
}

int main() {
  pre();
  int t;
  scanf("%d", &t);
  while (t-- > 0) work();
  return 0;
}