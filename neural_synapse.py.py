import math
import random
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neural Synapse Animation")

clock = pygame.time.Clock()


class Node:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.base_radius = random.randint(4, 8)
    self.angle = random.uniform(0, 2 * math.pi)
    self.speed = random.uniform(0.02, 0.05)


class SynapseAnimation:

  def __init__(self):
    self.center_x = WIDTH // 2
    self.center_y = HEIGHT // 2
    self.nodes = []

    # Create branching nodes radiating from the center
    for _ in range(30):
      distance = random.randint(50, 250)
      angle = random.uniform(0, 2 * math.pi)
      x = self.center_x + math.cos(angle) * distance
      y = self.center_y + math.sin(angle) * distance
      self.nodes.append(Node(x, y))

  def run(self):
    running = True
    time_counter = 0

    while running:
      screen.fill((5, 5, 10))  # Dark background simulating space/neural void

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      time_counter += 0.05

      # Pulsing effect for the central core
      core_radius = 20 + int(math.sin(time_counter * 2) * 5)

      # Draw connecting lines (synapses)
      for node in self.nodes:
        # Dynamic color shifting between cyan, green, and magenta
        r = int((math.sin(time_counter + node.x) + 1) * 100 + 50)
        g = int((math.cos(time_counter + node.y) + 1) * 63.5 + 128)
        b = 200

        # Draw synapse branch
        pygame.draw.line(
            screen, (r, g, b), (self.center_x, self.center_y), (node.x, node.y), 2
        )

        # Draw outer node
        pygame.draw.circle(
            screen, (r, g, b), (int(node.x), int(node.y)), node.base_radius
        )

      # Draw central glowing core
      pygame.draw.circle(
          screen, (255, 255, 200), (self.center_x, self.center_y), core_radius
      )
      pygame.draw.circle(
          screen,
          (100, 255, 150),
          (self.center_x, self.center_y),
          core_radius + 10,
          width=1,
      )

      pygame.display.flip()
      clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
  sim = SynapseAnimation()
  sim.run()