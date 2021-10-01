from IPython.display import SVG
import random
class Structure:
    def __init__(self, width):
        self.width = width
        self.height = random.randint(width, 5*width)
        capacity_percent = 0
        if width > 10:
            min_capacity = .5
        elif width > 5:
            min_capacity = .3
        else:
            min_capacity = 0.1
        while capacity_percent < min_capacity:
            self.structure = [random.randint(1, self.height) for _ in range(self.width)]
            capacity_percent = self._energy_capacity()/(self.width * self.height)

        self.svg_height = 600
        self.cwidth = self.svg_height/self.height
        self.main_template = '''
        <svg width="{width:d}" height="{height:d}">
            <style>
                svg{{
                    font-color:black;
                    font-size:20;
                    background-image: url(painting.png);
                    background-repeat: no-repeat;
                    background-size: {width:d}px {height:d}px;
                }}
                rect{{
                    fill:transparent;
                    stroke:grey;
                }}
                
                rect.block{{
                    fill:yellow;
                    stroke:yellow;
                }}
                rect.energy{{
                    fill:cyan;
                    stroke:cyan;
                }}
                rect.spill{{
                    fill:DeepPink;
                    stroke:DeepPink;
                }}
            </style>
            {content}
        </svg>
        '''
        self.square_template = '<rect x="{{x}}" y="{{y}}" width="{cwidth}" height="{cwidth}" class="{{kind}}"/>'.format(cwidth=self.cwidth)
      
    
    def supply_energy(self, energy):
        return self._draw(energy)
        
    def _draw(self, energy_supply = 0, column=None):
        result = []
        maxl, maxr = self._tower_table()
        over_supply = energy_supply - self._energy_capacity()
        for r in list(range(self.height))[::-1]:
            for c in range(self.width):
                kind = ""
                if column is not None and column != c:
                    pass
                else:
                    if (self.height-self.structure[c])<=r:
                        kind = "block"
                    elif (min(maxl[c],maxr[c]) - self.structure[c])>0 and self.height- min(maxl[c],maxr[c])<=r and energy_supply:
                        kind = "energy"
                        energy_supply -= 1
                    elif over_supply > 0:
                        kind = "spill"
                        over_supply -= 1
                    
                
                result += [self.square_template.format(x=c * self.cwidth, y=r * self.cwidth, kind=kind)]
                
        painting = self.main_template.format(width=int(self.width * self.cwidth), height=int(self.height * self.cwidth),
                                             content="\n".join(result))
        return SVG(painting)
    
    def view_column(self, column):
        return self.structure[column]
    
    def draw_column(self, column):
        return self._draw(column=column)
    
    def _tower_table(self):
        maxl = []
        for i in self.structure:
            maxl.append(max(maxl+[i]))
        
        maxr = []
        for i in self.structure[::-1]:
            maxr.append(max(maxr+[i]))
            
        return maxl, maxr[::-1]
    
    def _energy_capacity(self):
        maxl, maxr = self._tower_table()
        table = list(zip(maxl, maxr, self.structure))
        capacity = 0
        for l, r, height in table:
            capacity += min(l,r) - height

        return capacity