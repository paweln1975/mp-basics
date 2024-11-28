"""
gen for python files
>>> import sys; sys.tracebacklimit = 0
>>> c = 500
>>> gen_test_fac_method(c)
>>> gen_test_fac_method_signature(c)
>>> gen_fac_tests(c)
"""


def gen_test_fac_method(count: int):
    method_body = """
int facREPLACE(int n) {
    if (n==1 || n==0) {
        return 1;
    }
    else {
        return n * facREPLACE(n - 1);
    }    
}
"""
    save_generated_text(method_body, "methods.txt", count)


def gen_test_fac_method_signature(count: int):
    method_body = """int facREPLACE(int n);
"""
    save_generated_text(method_body, "signatures.txt", count)


def gen_fac_tests(count: int):
    test_method_body = """
TEST(FactorialTest, GeneratedFactorialValueREPLACE) {
	EXPECT_EQ(facREPLACE(4), 24);
}
"""
    save_generated_text(test_method_body, "tests.txt", count)


def save_generated_text(method_body: str, filename: str, count: int):
    method_list = [method_body.replace("REPLACE", str(i)) for i in range(1, count + 1)]
    with open(filename, 'w') as file:
        for element in method_list:
            file.write(element)
    file.close()
