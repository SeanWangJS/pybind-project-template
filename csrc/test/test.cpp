#include <gtest/gtest.h>

#include "ops.h"

TEST(ops, test_add_int) {

    int a = 1;
    int b = 2;
    int c = ops::add<int>(a, b);

    EXPECT_EQ(c, a + b);

}