from fractions import Fraction
from calculus_engine import *

calculus_type = int(input("Differentiation or Integration?(1/2):"))
if calculus_type ==  1:
  polynomial_type = int(input("Quadratic or Cubic?(1/2):"))
  if polynomial_type == 1:
    poly_coeffs = input("Enter the coefficients of your polynomial seperated by comma \n:").split(",")
    poly_coeffs_frac = [Fraction(i) for i in poly_coeffs]
    output = differentiation(poly_coeffs_frac , 1)
    print(output)
  else:
    poly_coeffs = input("Enter the coefficients of your polynomial seperated by comma \n:").split(",")
    poly_coeffs_frac = [Fraction(i) for i in poly_coeffs]
    output = differentiation(poly_coeffs_frac , 2)
    print(output)
else:
  inut = input()
  polynomial_type = int(input("Quadratic or Cubic?(1/2):"))
  if polynomial_type == 1:
    poly_coeffs = inut("Enter the coefficients of your polynomial seperated by comma \n:").split(",")
    poly_coeffs_frac = [Fraction(i) for i in poly_coeffs]
    output = integration(poly_coeffs_frac , 1)
    print(output)
  else:
    poly_coeffs = input("Enter the coefficients of your polynomial seperated by comma \n:").split(",")
    poly_coeffs_frac = [Fraction(i) for i in poly_coeffs]
    output = integration(poly_coeffs_frac , 2)
    print(output)
  