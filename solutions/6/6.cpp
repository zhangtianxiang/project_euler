#include <bits/stdc++.h>

#define kN 10010LL

long long ans[kN];

inline void prepare() {
  long long pre = 0;
  for (long long i = 1; i <= 10000; i++) {
    pre += i * i;
    ans[i] = (i * (i + 1) / 2) * (i * (i + 1) / 2) - pre;
  }
}

inline void work() {
  int n;
  scanf("%d", &n);
  printf("%lld\n", ans[n]);
}

int main() {
  int t;
  prepare();
  scanf("%d", &t);
  while (t--) work();
  return 0;
}