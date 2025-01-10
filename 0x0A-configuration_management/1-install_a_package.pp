/* Using Puppet, install flask from pip3.

Requirements:

- Install flask
- Version must be 2.1.0 */

package { 'Flask':
  provider => 'pip3',
  ensure => "2.1.0"
}
