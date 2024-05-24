#include <gtest/gtest.h>

#include "ops.h"

TEST(ops, test_add_int) {

    int a = 1;
    int b = 2;
    int c = ops::add<int>(a, b);

    EXPECT_EQ(c, a + b);

}

TEST(ops, test_add_float) {

    float a = 1.0;
    float b = 2.0;
    float c = ops::add<float>(a, b);

    EXPECT_EQ(c, a + b);

}