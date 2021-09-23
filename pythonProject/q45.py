word_of_string = """bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk 
darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent 
jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass 
petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet 
sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko 
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"""
empty_list = []
empty_string = ""
counter = 0
spliter_string = word_of_string.split()
for i in spliter_string:
    if counter == 0:
      empty_list.append(i)
      empty_string = i[-1]
      counter += 1
    if i in empty_list:
         for j in spliter_string[counter:]:
            if j[0] == empty_string:
                empty_list.append(j)
                empty_string = j[-1]
print(empty_list)