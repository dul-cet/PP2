"""
1. A recipe you are reading states how many grams you need for the ingredient.
Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. 
`ounces = 28.3495231 * grams` """
def convert(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input())
print(convert(grams))