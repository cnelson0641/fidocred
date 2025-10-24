output "vpc_id" {
    value = aws_vpc.fidocred_vpc.id
}

output "public_subnet_1_id" {
    value = aws_subnet.public_subnet1.id
}

output "private_subnet_2_id" {
    value = aws_subnet.private_subnet2.id
}
