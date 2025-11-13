from pyscript import display

band = {'Erin', 'Juanico', 'Lan', 'JM'}
basketball = {'Oscar', 'Gur', 'Inigo', 'JM', 'Juanico'}

display(band | basketball, target="output")  # union
display(band & basketball, target="output")  # intersection
display(band - basketball, target="output")  # difference
display(basketball - band, target="output")  # difference
display(band ^ basketball, target="output")  # symmetric difference

