#include <bits/stdc++.h>

#define kN 45LL

long long ans[kN];

void work() {
  int n;
  scanf("%d", &n);
  printf("%lld\n", ans[n]);
}

void prepare() {
  ans[1] = 1;
  ans[2] = 2;
  ans[3] = 6;
  long long gcd;
  for (int i = 4; i <= 40; i++) {
    gcd = std::__gcd(ans[i - 1], (long long)i);
    ans[i] = i / gcd * ans[i - 1];
  }
}

int main() {
  int t;
  prepare();
  scanf("%d", &t);
  while (t-- > 0) {
    work();
  }
  return 0;
}
