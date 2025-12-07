def differentiation(coeffs , poly_type):
  if poly_type == 1:
    print(f"Your quadratic function is \n{coeffs[0]}x² + {coeffs[1]}x + {coeffs[2]}")
    quad_term_1 = coeffs[0] * 2
    quad_term_2 = coeffs[1]
    return f"The derivative of your quadratic function is \n{quad_term_1}x + {quad_term_2}"
  else:
    print(f"Your cubic function is \n{coeffs[0]}x³ + {coeffs[1]}x² + {coeffs[2]}x + {coeffs[3]}")
    cube_term_1 = coeffs[0] * 3
    cube_term_2 = coeffs[1] * 2
    cube_term_3 = coeffs[2]
    return f"The derivative of your cubic function is \n{cube_term_1}x² + {cube_term_2}x + {cube_term_3}"
  
def integration(coeffs , poly_type):
  if poly_type ==  1:
    print(f"∫{coeffs[0]}x² + {coeffs[1]}x + {coeffs[2]}dx")
    quad_term_1 = coeffs[0] / 3
    quad_term_2 = coeffs[1] / 2
    quad_term_3 = coeffs[2]
    return f"the integral of your quadratic function is \n {quad_term_1}x³ + {quad_term_2}x² + {quad_term_3}x + c"
  else:
    print(f"∫{coeffs[0]}x³ + {coeffs[1]}x² + {coeffs[2]}x + {coeffs[3]}dx")
    cube_term_1 = coeffs[0] / 4
    cube_term_2 = coeffs[1] / 3
    cube_term_3 = coeffs[2] / 2
    cube_term_4 = coeffs[3]
    return f"The derivative of your cubic function is \n{cube_term_1}x⁴ + {cube_term_2}x³ + {cube_term_3}x² + {cube_term_4} + c"
  
    