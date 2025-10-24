module "network" {
  source = "./network"
}

module "db" {
  source     = "./db"
  depends_on = [module.network]

  # Network
  vpc_id = module.network.vpc_id
  private_subnet_id = module.network.private_subnet_id
}

module "app" {
  source     = "./app"
  depends_on = [module.db]

  # Network
  vpc_id            = module.network.vpc_id
  public_subnet_id  = module.network.public_subnet_id
  private_subnet_id = module.network.private_subnet_id

  # DB
  db_sg_id = module.db.db_sg_id
}
