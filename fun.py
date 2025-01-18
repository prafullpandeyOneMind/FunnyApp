code = """
def example_function():
    x = 10
    return y  # undefined variable
"""

results = analyze_code(code)
print(results)
