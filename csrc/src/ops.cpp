#include "ops.h"

namespace ops
{

template <typename scalar_t>
scalar_t add(scalar_t a, scalar_t b) {
    return a + b;
}

// template specialization
template int add<int>(int a, int b);
template float add<float>(float a, float b);
template double add<double>(double a, double b);

    
} // namespace ops
