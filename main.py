# main.py

from class_static_methods_demo import Calculator

def main():
    print("--- Testing Calculator Methods ---")

    # 1. Using the static method
    # It is called on the class but requires no class-specific data.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    
    # 2. Using the class method
    # It is called on the class and uses the 'cls' parameter to access the class attribute.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()