##################
# VPC
##################
# VPC
resource "aws_vpc" "fidocred_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
}

# Public Subnet for Lambda
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.fidocred_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
}

# Private Subnet for DB
resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.fidocred_vpc.id
  cidr_block        = "10.0.2.0/24"
}

# Internet Gateway for Lambda egress
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.fidocred_vpc.id
}

# Public Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.fidocred_vpc.id
}

# Public Route mapping to public subnet (0.0.0.0/0 to IGW)
resource "aws_route" "public_internet_route" {
  route_table_id         = aws_route_table.public_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.igw.id
}

# Associate public subnet with public route table
resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# Private Route Table
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.fidocred_vpc.id
}

# Associate private subnet with private route table
resource "aws_route_table_association" "private_assoc" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_rt.id
}
