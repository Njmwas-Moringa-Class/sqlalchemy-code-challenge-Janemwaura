import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Restaurant, Review

@click.group()
def cli():
    """Restaurant CLI"""


@cli.command()
def initdb():
    """Initialize the database"""
    engine = create_engine('sqlite:///db/restaurants.db', echo=True)
    Base.metadata.create_all(engine)
    click.echo("Database initialized")


@cli.command()
@click.option('--name', prompt='Restaurant name', help='The name of the restaurant')
@click.option('--price', prompt='Restaurant price', help='The price range of the restaurant')
def add_restaurant(name, price):
    """Add a new restaurant"""
    engine = create_engine('sqlite:///db/restaurants.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    restaurant = Restaurant(name=name, price=price)
    session.add(restaurant)
    session.commit()
    click.echo(f"Added restaurant: {name}")


@cli.command()
@click.option('--first_name', prompt='Customer first name', help='The first name of the customer')
@click.option('--last_name', prompt='Customer last name', help='The last name of the customer')
def add_customer(first_name, last_name):
    """Add a new customer"""
    engine = create_engine('sqlite:///db/restaurants.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    customer = Customer(first_name=first_name, last_name=last_name)
    session.add(customer)
    session.commit()
    click.echo(f"Added customer: {first_name} {last_name}")


if __name__ == '__main__':
    cli()
