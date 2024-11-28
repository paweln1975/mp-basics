"""
gen for python files
>>> import sys; sys.tracebacklimit = 0
>>> c = 500
>>> gen_test_fib_method(c)
>>> gen_test_fib_method_signature(c)
>>> gen_fib_tests(c)
"""


def gen_test_fib_method(count: int):
    method_body = """
int fibREPLACE(int n) {
    int t1 = 0, t2 = 1, nextTerm = 0;
    for (int i = 1; i <= n; ++i) {
    nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    return nextTerm;
}
"""
    save_generated_text(method_body, "methods.txt", count)


def gen_test_fib_method_signature(count: int):
    method_body = """int fibREPLACE(int n);
"""
    save_generated_text(method_body, "signatures.txt", count)


def gen_fib_tests(count: int):
    test_method_body = """
TEST(FibonacciTest, HandleGeneratedCaseREPLACE) {
	EXPECT_EQ(fibREPLACE(8), 34);
}
"""
    save_generated_text(test_method_body, "tests.txt", count)


def save_generated_text(method_body: str, filename: str, count: int):
    method_list = [method_body.replace("REPLACE", str(i)) for i in range(1, count + 1)]
    with open(filename, 'w') as file:
        for element in method_list:
            file.write(element)
    file.close()
