# mysql-connector-python                     # Official MySQL connector. Pure Python and very simple.
# from mysql.connector import connect, Error  # Import connect to open the database and Error to catch problems.
# from sqlalchemy import text                 # text() lets you safely write SQL commands inside Python.
#
# try:                                        # Try to run this block of code.
#     conn = connect(                          # Open a connection to the database.
#         host="localhost",                    # Database is on your computer.
#         user="root",                         # MySQL username.
#         password="your_password",            # Replace with your own password.
#         database="your_db"                   # The database you want to use.
#     )
#     conn.cursor().execute("UPDATE table_name SET column1='value' WHERE id=1")  # Run an SQL update.
#     conn.commit()                            # Save the change so it stays in the table.
# except Error as e:                            # If something goes wrong (wrong password, etc.).
#     print(e)                                  # Print the problem on the screen.
# finally:                                      # This always runs at the end.
#     conn.close()                              # Close the connection to free resources.
#
# ------------------------------------------------------------
#
# pymysql                                     # Pure Python connector for MySQL. Easy and works with pandas or SQLAlchemy.
# import pymysql                               # Import the PyMySQL package.
# from sqlalchemy import text                  # text() lets you write SQL commands.
#
# try:                                         # Try to run this block of code.
#     conn = pymysql.connect(                  # Open a connection to the database.
#         host="localhost",                    # Database is on your computer.
#         user="root",                         # MySQL username.
#         password="your_password",            # Your password here.
#         database="your_db"                   # Name of the database.
#     )
#     with conn.cursor() as cursor:            # Use the cursor to run SQL commands.
#         cursor.execute("UPDATE table_name SET column1='value' WHERE id=1")  # Run an SQL update.
#     conn.commit()                             # Save the change so it stays.
# except Exception as e:                        # If something goes wrong.
#     print(e)                                  # Print the problem.
# finally:                                      # Always runs at the end.
#     conn.close()                              # Close the connection.
#
# ------------------------------------------------------------
#
# mysqlclient (MySQLdb)                        # C-based connector. Faster but harder to install.
# import MySQLdb                                # Import the MySQLdb driver.
# from sqlalchemy import text                   # text() is for writing SQL commands.
#
# try:                                          # Try to run this block.
#     conn = MySQLdb.connect(                   # Open the database connection.
#         host="localhost",                     # Database is on your computer.
#         user="root",                          # Your MySQL username.
#         passwd="your_password",               # Your password here.
#         db="your_db"                          # The database you want.
#     )
#     cursor = conn.cursor()                     # Create a cursor for SQL commands.
#     cursor.execute("UPDATE table_name SET column1='value' WHERE id=1")  # Run the update.
#     conn.commit()                               # Save the change.
# except Exception as e:                          # If something goes wrong.
#     print(e)                                    # Print the error message.
# finally:                                        # Always runs at the end.
#     conn.close()                                # Close the connection.
#
# ------------------------------------------------------------
#
# SQLAlchemy + PyMySQL                          # Good if you like pandas or ORM style. Very flexible.
# from sqlalchemy import create_engine, text     # create_engine builds a connection; text lets you write SQL.
# engine = create_engine("mysql+pymysql://root:your_password@localhost/your_db")  # Connection link to MySQL.
#
# try:                                           # Try to run this block.
#     with engine.connect() as conn:             # Open and manage the connection.
#         conn.execute(text("UPDATE table_name SET column1='value' WHERE id=1"))  # Run the update.
#         conn.commit()                           # Save the change.
# except Exception as e:                           # If something goes wrong.
#     print(e)                                     # Print the problem.
# finally:                                         # Always runs at the end.
#     engine.dispose()                              # Close and clean the engine connection.
#
# ------------------------------------------------------------
#
# SQLAlchemy + mysql-connector                   # Same as above but uses mysql-connector inside.
# from sqlalchemy import create_engine, text      # Import create_engine and text for SQL.
# engine = create_engine("mysql+mysqlconnector://root:your_password@localhost/your_db")  # Connection with mysql-connector.
#
# try:                                            # Try to run this block.
#     with engine.connect() as conn:              # Open the connection.
#         conn.execute(text("UPDATE table_name SET column1='value' WHERE id=1"))  # Run the update.
#         conn.commit()                             # Save the change.
# except Exception as e:                             # If something goes wrong.
#     print(e)                                       # Print the problem.
# finally:                                           # Always runs at the end.
#     engine.dispose()                                # Close the engine connection.
#
# ------------------------------------------------------------
#
# SQLAlchemy + mysqlclient                        # Same but uses MySQLdb inside.
# from sqlalchemy import create_engine, text       # Import create_engine and text.
# engine = create_engine("mysql+mysqldb://root:your_password@localhost/your_db")  # Use MySQLdb as the driver.
#
# try:                                             # Try to run this block.
#     with engine.connect() as conn:               # Open the connection.
#         conn.execute(text("UPDATE table_name SET column1='value' WHERE id=1"))  # Run the update.
#         conn.commit()                              # Save the change.
# except Exception as e:                               # If something goes wrong.
#     print(e)                                         # Print the problem.
# finally:                                             # Always runs at the end.
#     engine.dispose()                                  # Close the engine.
#
# ------------------------------------------------------------
#
# aiomysql                                        # Async (runs tasks at the same time). Advanced use.
# import asyncio, aiomysql                         # Import asyncio (for async code) and aiomysql.
#
# async def run():                                  # Define an async function to handle the work.
#     try:                                          # Try to run this block.
#         conn = await aiomysql.connect(           # Open the database connection asynchronously.
#             host="localhost",
#             user="root",
#             password="your_password",
#             db="your_db"
#         )
#         async with conn.cursor() as cur:         # Use an async cursor.
#             await cur.execute("UPDATE table_name SET column1='value' WHERE id=1")  # Run the update.
#         await conn.commit()                       # Save the change.
#     except Exception as e:                         # If something goes wrong.
#         print(e)                                   # Print the problem.
#     finally:                                       # Always runs at the end.
#         conn.close()                               # Close the connection.
#
# asyncio.run(run())                                 # Start the async function.
#
# ------------------------------------------------------------
#
# torndb                                          # Light tool built on PyMySQL. Used with Tornado web apps.
# import torndb                                    # Import torndb.
#
# try:                                             # Try to run this block.
#     db = torndb.Connection(                      # Open the database connection.
#         host="localhost",
#         database="your_db",
#         user="root",
#         password="your_password"
#     )
#     db.execute("UPDATE table_name SET column1='value' WHERE id=1")  # Run the update.
# except Exception as e:                             # If something goes wrong.
#     print(e)                                       # Print the problem.
# finally:                                           # Always runs at the end.
#     db.close()                                     # Close the connection.
#
# ------------------------------------------------------------
#
# oursql                                          # Older connector. Similar to others but less common now.
# import oursql                                    # Import oursql.
#
# try:                                             # Try to run this block.
#     conn = oursql.connect(                       # Open the database connection.
#         host="localhost",
#         user="root",
#         passwd="your_password",
#         db="your_db"
#     )
#     cursor = conn.cursor()                        # Create a cursor to run SQL commands.
#     cursor.execute("UPDATE table_name SET column1='value' WHERE id=1")  # Run the update.
#     conn.commit()                                  # Save the change.
# except Exception as e:                              # If something goes wrong.
#     print(e)                                       # Print the problem.
# finally:                                           # Always runs at the end.
#     conn.close()                                   # Close the connection.
