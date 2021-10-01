import random
from collections import Counter, namedtuple

from graphviz import ExecutableNotFound

Schematic = namedtuple("Schematic", ['instructions', 'edges'])


def random_string():
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(random.randint(3, 5))).upper()


def get_instruction_codes(instructions):
    instruction_codes = set()
    for _ in instructions:
        code = random_string()
        while code in instruction_codes:
            code = random_string()
        instruction_codes.add(code)
    return list(instruction_codes)


def generate_schematic(start_lenght=200):
    edges = []
    instructions = list(range(start_lenght))[::-1]
    leaves = set(instructions)
    picked = Counter()
    instructions_left = list(instructions)

    while instructions_left:
        node = instructions_left.pop()
        if instructions_left:
            select_from = set(instructions_left) - set(k for k, v in picked.items() if v > 1)
            if select_from:
                upper_bound = min(len(select_from), 3)
                targets = random.sample(select_from, random.randint(1, upper_bound))
                picked.update(targets)
                leaves -= {node}
                for target in targets:
                    edges.append((node, target))

    while len(leaves) > 1:
        upper_bound = min(len(leaves), 3)
        sources = random.sample(leaves, random.randint(1, upper_bound))
        leaves -= set(sources)
        target = max(instructions) + 1
        instructions.append(target)
        leaves.add(target)
        for source in sources:
            edges.append((source, target))
    instruction_codes = get_instruction_codes(instructions)

    instructions = [instruction_codes[x] for x in instructions]
    random.shuffle(instructions)

    edges = [(instruction_codes[e[0]], instruction_codes[e[1]]) for e in edges]
    random.shuffle(edges)

    return Schematic(instructions=sorted(instructions), edges=edges)


class GraphvizInstallation:
    @staticmethod
    def _repr_html_():
        return '''
                How to install graphviz:
                <ol>
          <li>Install graphviz<br/>(<a class="reference external" href="https://www.graphviz.org/download/">download page</a>,
        <a class="reference external" href="https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224">installation procedure for Windows</a>)</li>
          <li>Install the pure-Python interface for the Graphviz<br/>
          <pre>$ pip install graphviz
        </pre></li>
        </ol>
              <i>Summarized from the offical graphviz <a class="headerlink" href="https://graphviz.readthedocs.io/en/stable/manual.html#installation" title="Permalink to this headline">documentation</a>:</i>
                        <hr/>
                        <div class="section" id="installation">
        <h2>Installation</h2>
        <p><code class="xref py py-mod docutils literal notranslate"><span class="pre">graphviz</span></code> provides a simple pure-Python interface for the <a class="reference external" href="https://www.graphviz.org">Graphviz</a>
        graph-drawing software. It runs under Python 2.7 and 3.6+. To install it
        with <a class="reference external" href="https://pip.readthedocs.io">pip</a> run the following:</p>
        <div class="highlight-bash notranslate"><div class="highlight"><pre>$ pip install graphviz
        </pre></div>
        </div>
        <p>For a system-wide install, this typically requires administrator access. For an
        isolated install, you can run the same inside a <a class="reference external" href="https://virtualenv.pypa.io">virtualenv</a> or a
        <a class="reference external" href="https://docs.python.org/3/library/venv.html#module-venv" title="(in Python v3.9)"><code class="docutils literal notranslate"><span class="pre">venv</span></code></a> (Python 3 only).</p>
        <p>The only dependency is a working installation of Graphviz (<a class="reference external" href="https://www.graphviz.org/download/">download page</a>,
        <a class="reference external" href="https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224">installation procedure for Windows</a>).</p>
        <p>After installing Graphviz, make sure that its <code class="docutils literal notranslate"><span class="pre">bin/</span></code> subdirectory containing
        the layout commands for rendering graph descriptions (<code class="docutils literal notranslate"><span class="pre">dot</span></code>, <code class="docutils literal notranslate"><span class="pre">circo</span></code>,
        <code class="docutils literal notranslate"><span class="pre">neato</span></code>, etc.) is on your systems’ path: On the command-line, <code class="docutils literal notranslate"><span class="pre">dot</span> <span class="pre">-V</span></code>
        should print the version of your Graphiz installation.</p>
        </div>
                           <hr/>
         '''


def visualize_schematic(schematic: Schematic):
    try:
        from graphviz import Digraph

        dot = Digraph(comment='The Factory', format='png')
        dot.edges([(str(e1), str(e2)) for e1, e2 in schematic.edges])
        dot.render()
        return dot

    except ExecutableNotFound:
        print("Graphviz executable not found.\nTake an extra look at step 1. "
              "It looks like the /bin subdirectory is not on your systems path.")
        return GraphvizInstallation()

    except ImportError:
        print("Could not import the visualization package.")
        return GraphvizInstallation()


schematic = generate_schematic()
