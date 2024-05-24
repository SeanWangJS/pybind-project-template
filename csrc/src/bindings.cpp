#include <pybind11/pybind11.h>

#include "ops.h"

#if not defined(OPS_PYBIND_MODULE)
#error "OPS_PYBIND_MODULE not defined"
#endif

PYBIND11_MODULE(OPS_PYBIND_MODULE, m) {
    m.doc() = "Ops Python Bindings for C++";

    m.def("add", &ops::add<int>, pybind11::arg("a"), pybind11::arg("b"), "Add two integers");

    m.def("add", &ops::add<float>, pybind11::arg("a"), pybind11::arg("b"), "Add two floats");

    m.def("add", &ops::add<double>, pybind11::arg("a"), pybind11::arg("b"), "Add two doubles");
    
}