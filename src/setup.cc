#include "setup.h"

#include <impeller.hpp>
#include <map>
#include <mutex>

namespace IMPELLER_HPP_NAMESPACE {
ProcTable gGlobalProcTable;
}  // namespace IMPELLER_HPP_NAMESPACE

namespace impeller::py {

static void SetupImpellerHPPProcTableOnce() {
  static std::once_flag sOnceFlag;
  std::call_once(sOnceFlag, []() {
    std::map<std::string, void*> proc_map;
#define IMPELLER_HPP_PROC(name) \
  proc_map[#name] = reinterpret_cast<void*>(&name);
    IMPELLER_HPP_EACH_PROC(IMPELLER_HPP_PROC)
#undef IMPELLER_HPP_PROC
    impeller::hpp::gGlobalProcTable.Initialize(
        [&](auto name) { return proc_map.at(name); });
  });
}

void SetupOnce() {
  SetupImpellerHPPProcTableOnce();
}

}  // namespace impeller::py
