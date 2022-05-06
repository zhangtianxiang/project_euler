#include <bits/stdc++.h>

#define kN 10010LL
#define kMax 104743LL  // 这个手动二分

int pri[kN], cnt;
bool notpri[kMax + 1];

inline void sieve() {
  for (int i = 2, j; i <= kMax; i++) {
    if (!notpri[i]) pri[++cnt] = i;
    for (j = 1; j <= cnt; j++) {
      if (pri[j] * i > kMax) break;
      notpri[pri[j] * i] = true;
      if (i % pri[j] == 0) break;
    }
  }
}

int main() {
  sieve();
  int t, x;
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &x);
    printf("%d\n", pri[x]);
  }
  return 0;
}