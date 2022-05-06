#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

from cgitb import html
from common import *

import traceback
from urllib import request
from bs4 import BeautifulSoup
import os


mathjax_script = '''<script>
  if (typeof MathJax === 'undefined') {
    window.MathJax = {
      loader: {
        source: {
          '[tex]/amsCd': '[tex]/amscd',
          '[tex]/AMScd': '[tex]/amscd'
        }
      },
      tex: {
        inlineMath: {'[+]': [['$', '$']]},
        tags: 'ams'
      },
      options: {
        renderActions: {
          findScript: [10, doc => {
            document.querySelectorAll('script[type^="math/tex"]').forEach(node => {
              const display = !!node.type.match(/; *mode=display/);
              const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
              const text = document.createTextNode('');
              node.parentNode.replaceChild(text, node);
              math.start = {node: text, delim: '', n: 0};
              math.end = {node: text, delim: '', n: 0};
              doc.math.push(math);
            });
          }, '', false],
          insertedScript: [200, () => {
            document.querySelectorAll('mjx-container').forEach(node => {
              let target = node.parentNode;
              if (target.nodeName.toLowerCase() === 'li') {
                target.parentNode.classList.add('has-jax');
              }
            });
          }, '', false]
        }
      }
    };
    (function () {
      var script = document.createElement('script');
      script.src = '//cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
      script.defer = true;
      document.head.appendChild(script);
    })();
  } else {
    MathJax.startup.document.state(0);
    MathJax.texReset();
    MathJax.typeset();
  }
</script>'''


def fetch_en(id):
    en_prob_addr = f'https://projecteuler.net/problem={id}'
    rsp = request.urlopen(en_prob_addr)
    assert rsp.getcode() == 200
    raw = rsp.read()
    soup = BeautifulSoup(raw, 'html.parser')
    res = soup.find(id='content')
    assert res != None
    prob_desc = res.find(class_='problem_content')
    prob_name = res.find('h2')
    html_part = f'<h1><a href="{en_prob_addr}">原始项目</a></h1>' + \
        str(prob_name) + str(prob_desc) + '<hr />'
    return html_part


def fetch_cn(id):
    cn_prob_addr = f'http://pe-cn.github.io/{id}/'
    rsp = request.urlopen(cn_prob_addr)
    assert rsp.getcode() == 200
    raw = rsp.read()
    soup = BeautifulSoup(raw, 'html.parser')
    res = soup.find(class_='post-body')
    assert res != None
    title = res.find('h1')
    if title != None:
        title.extract()
    bar = res.find('hr')
    if bar != None:
        bar.extract()
    bar = res.find('hr')
    if bar != None:
        bar.extract()

    html_part = f'<h1><a href="{cn_prob_addr}">中文翻译站</a></h1>' + str(res)
    return html_part


def fetch_oj(id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    oj_prob_addr = 'https://www.hackerrank.com/contests/projecteuler/challenges/euler{:03d}/problem'.format(
        int(id))
    req = request.Request(oj_prob_addr, headers=headers)
    rsp = request.urlopen(req)
    assert rsp.getcode() == 200
    raw = rsp.read()
    soup = BeautifulSoup(raw, 'html.parser')
    res = soup.find(class_='challenge-body-html')
    assert res != None
    sub = res.find('sub')
    if sub != None:
        sub.extract()
    html_part = f'<h1><a href="{oj_prob_addr}" >HackerRank</a></h1>' + \
        str(res) + '<hr />'
    return html_part


def main():
    id, dir = arg_id_dir()
    part_orginal = fetch_en(id)
    part_translate = fetch_cn(id)
    part_online_judge = fetch_oj(id)
    generate_html(id, dir, part_orginal, part_translate, part_online_judge)


def generate_html(id, dir, *args):
    parent = f'{os.path.join(dir,id)}'
    if not os.path.exists(parent):
      os.mkdir(parent)
    with open(f'{parent}/{id}.html', 'w') as f:
        f.write('''<!DOCTYPE html><html lang="zh-CN">''')
        f.write('''<body>''')
        for arg in args:
            f.write(arg)
        f.write(mathjax_script)
        f.write('''</body>''')
        f.write('''</html>''')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint('\nStopped', red)
    except Exception as e:
        cprint('\nError', red)
        traceback.print_exc()
