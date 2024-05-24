from Barcode.capture_barcode import capture_barcode 
from Product.Required_JSON import call_api
from Product.Display_Product_Info import display_product_info 
from Health_Score.Health_Score_Generator import evaluate_health



def main():
   print("Scanning for barcode...")
   barcode= capture_barcode()
   print(type(barcode))
   if barcode:
      print(f"Barcode detected: {barcode}")
      print("\nFetching product information...")
      response= call_api(barcode)
      if response:
         display_product_info(response)
         Health_Score, eco_grade, explanation, def_nutri, suf_nutri, exc_nutri=evaluate_health(response)
         print("Health Score Achieved: ", Health_Score)
         print("Grade Achieved: ", eco_grade.capitalize())
         print('\nNutrient Analysis-:')
         print("Deficient Nutrients: ", def_nutri)
         print("Sufficient Nutrients: ", suf_nutri)
         print("Excessive Nutrients: ", exc_nutri)
         print("\nInference", explanation)

   # res= call_api("8901058904741")
   # print(res)
   # evaluate_health(res)





main()