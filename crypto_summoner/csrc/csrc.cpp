// binary
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
using namespace std;
namespace py = pybind11;

bool nonzero(py::list aList){
    for (auto &item: aList)
        // Casting 0 to a Python object, so as to compare it with the list's contents
        if (item.is(py::cast(0)))
            return false;
    return true;
}

PYBIND11_MODULE(csrc, m){
    m.doc() = "introducing pybind11";
    m.def("nonzero", &nonzero,
          "Operate on integer list; return True if nonzero element exists",
          py::arg("aList"));
}
// int main ()
// {
//   return 0;
// }