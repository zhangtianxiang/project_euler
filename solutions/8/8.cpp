#include <bits/stdc++.h>

#define kN 1010LL

char s[kN];

inline void work() {
  int n, k;
  scanf("%d%d", &n, &k);
  scanf("%s", s);
  long long now = 1, max = 0;
  for (int i = 0; i < k; i++) {
    now *= s[i] - '0';
  }
  max = now;
  for (int i = k, j; i < n; i++) {
    now = 1;
    for (j = i - k + 1; j <= i; j++) now *= s[j] - '0';
    if (now > max) max = now;
  }
  printf("%lld\n", max);
}

int main() {
  int t;
  scanf("%d", &t);
  while (t--) work();
  return 0;
}