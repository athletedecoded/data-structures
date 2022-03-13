/* author @athletedecoded */
// The header file is the "interface" specification, like an API
# pragma once
#include <string>

using std::string;
namespace obj {
    class Cube {
        public:
            Cube(double length);  // One argument constructor

            int getLength() const;
            double getVolume() const;
            double getSurfaceArea() const;
            void setLength(double length);
            bool operator==(const Cube & other);

        private:
            double length_;
    };
}