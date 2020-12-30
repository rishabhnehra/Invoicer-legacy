import {Story, Meta} from '@storybook/react/types-6-0';

import {PriceCard, PriceCardProps} from './PriceCard';

export default {
    title: 'Components/Card',
    component: PriceCard
} as Meta;

const Template: Story<PriceCardProps> = (args) => <PriceCard {...args} />

export const Price = Template.bind({});
Price.args = {
    description: 'Description',
    itemType: 'Item type',
    quantity: 2,
    price: 99900
}